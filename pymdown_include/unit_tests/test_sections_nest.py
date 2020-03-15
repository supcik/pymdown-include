# Copyright 2020 Jacques Supcik
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from pathlib import Path

import markdown

from pymdown_include import PymdownInclude

MD = """\
# h1
{!sections.md!#}
## h2
{!sections.md!#}"""

HTML = """\
<h1>h1</h1>
<p>root</p>
<h2>head1</h2>
<p>text1</p>
<h3>head2</h3>
<p>text2</p>
<h2>h2</h2>
<p>root</p>
<h3>head1</h3>
<p>text1</p>
<h4>head2</h4>
<p>text2</p>"""


class Test(unittest.TestCase):

    def test(self):
        md = markdown.Markdown(
            extensions=[PymdownInclude(SEARCH_PATH=[Path(__file__).parent])])
        self.assertEqual(md.convert(MD), HTML)


if __name__ == '__main__':
    unittest.main()
