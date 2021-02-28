# Copyright 2018 Google Inc. All Rights Reserved.
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

import main

def test_1():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/')
    assert r.status_code == 200
    assert 'AAA10xCC' in r.data.decode('utf-8')

def test_2():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/about')
    assert r.status_code == 200
    assert 'This page is work in progress' in r.data.decode('utf-8')

def test_3():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/careers')
    assert r.status_code == 200
    assert 'This page is work in progress' in r.data.decode('utf-8')

def test_4():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/contact')
    assert r.status_code == 200
    assert 'This page is work in progress' in r.data.decode('utf-8')

def test_5():
    main.app.testing = True
    client = main.app.test_client()

    r = client.get('/#services')
    assert r.status_code == 200
    assert 'Consulting Services' in r.data.decode('utf-8')
