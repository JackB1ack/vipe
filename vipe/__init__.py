# Copyright 2013-2016 University of Warsaw
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

import os.path

__title__ = 'vipe'
__author__ = 'Mateusz Kobos'
__email__ = 'mkobos@icm.edu.pl'
__version__ = open(os.path.join(os.path.dirname(
    __file__), 'RELEASE-VERSION')).read().strip()
__description__ = 'Tool for visualizing Apache Oozie pipelines'
__license__ = 'Apache License, Version 2.0'
