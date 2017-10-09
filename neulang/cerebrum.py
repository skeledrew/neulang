# This file is part of neulang

# neulang - A language sitting on top of Python that executes pseudocode that's very close to natural language.

# @author Andrew Phillips
# @copyright 2017 Andrew Phillips <skeledrew@gmail.com>

# neulang is free software; you can redistribute it and/or
# modify it under the terms of the GNU AFFERO GENERAL PUBLIC LICENSE
# License as published by the Free Software Foundation; either
# version 3 of the License, or any later version.

# neulang is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU AFFERO GENERAL PUBLIC LICENSE for more details.

# You should have received a copy of the GNU Affero General Public
# License along with neulang.  If not, see <http://www.gnu.org/licenses/>.


import sys
import pdb
import re

import future


class Cerebrum():

    def __init__(self, populate=True):
        self._nuclei = {}
        self._thot_text = None
        self._thoughts = {
            'call_stack': [],
            'run_queue': [],
            'var_heap': {},
            'self': self,
        }
        self._neurons = []
        if populate: self.make_neurons()

    def make_neurons(self, *nuclei):
        if not nuclei: nuclei = [globals()[elem] for elem in globals() if elem.startswith('neu_')]
        cnt = 0

        for nucleus in nuclei:
            rx = nucleus()
            if not isinstance(rx, str): continue
            self._nuclei[rx] = nucleus
            cnt += 1
        return cnt

    def think(self):
        # usually a single neuron at the top
        if interact: pdb.set_trace()
        self._thoughts['last'] = [neuron.fire(self._thoughts) for neuron in self._neurons]
        return

    def read(self, text, style='org'):
        # convert text into neurons
        #if interact: pdb.set_trace()
        self._thot_text = text
        neuron_list = []
        indent = r'^\*+ '
        if isinstance(text, str): text = text.strip().split('\n')
        level = ''

        for line in text:
            # create neurons from text
            match = re.match(indent, line)
            if not level and match: level = match.group(0)
            if not level: continue
            if not re.match(indent, line): continue
            neuron = Neuron(' '.join(line.split(' ')[1:]), self._nuclei)
            level_cnt = line.split(' ')[0].count('*')
            neuron_list.append([level_cnt, neuron])
        self._neurons = self._make_neuron_tree(neuron_list)
        return len(text)

    def _make_neuron_tree(self, neuron_list, level_cnt=1):
        # takes a list of neurons with levels, and recursively creates a tree of neurons
        tree = []
        sub_tree = []
        curr_level = level_cnt

        for neuron in neuron_list:

            if neuron[0] == level_cnt:

                if sub_tree:
                    # recurse and connect to assoc neuron
                    tree[-1].attach(self._make_neuron_tree(sub_tree, level_cnt+1))
                    sub_tree = []

                else:
                    tree.append(neuron[1])

            elif neuron[0] > level_cnt:
                # build sublist
                sub_tree.append(neuron)

            else:
                # shouldn't be here
                raise Exception('shouldn\'t be here')
        return tree

class Neuron():

    def __init__(self, text, nuclei):
        self._chain = []
        self.build(text, nuclei)

    def __str__(self):
        return '{}'.format(self._rx)

    def __repr__(self):
        return '"Neuron(rx={})"'.format(self._rx)

    def build(self, text, nuclei):
        res = None
        self._text = text

        try:
            for rx in nuclei:
                match = re.match(rx, text)
                if not match: continue
                nucleus = nuclei[rx]
                self._rx = rx
                setattr(self, '_nucleus', nucleus.__get__(self, self.__class__))
            res = self

        except Exception as e:
            res = e
        return res

    def _nucleus(self):
        # just a stub
        pass

    def parse(self, text, ):
        pass

    def attach(self, nodes):
        self._chain.append(nodes)

    def fire(self, state):
        return self._nucleus(state)

    def get_text(self):
        return self._text

    def get_chain(self):
        return self._chain

    def gen(self):
        pass


def neu_print(*args):
    rx = r'print (?P<What>[\w ]+)'
    if not args: return rx
    self = args[0]
    what = re.match(rx, self.get_text()).group('What')
    print(what)
    return True

def create_cerebrum():
    return Cerebrum()


interact = False

if not __name__ == '__main__' and sys.argv[0] == '':
    # using interpreter
    interact = True