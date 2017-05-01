# ilorest Cookbook

[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/HewlettPackard/chef-ilorest-cookbook)
[![Chef cookbook](https://img.shields.io/cookbook/v/ilorest.svg)](https://supermarket.chef.io/cookbooks/ilorest)
[![license](https://img.shields.io/badge/license-Apache%202-blue.svg)](https://github.com/HewlettPackard/chef-ilorest-cookbook)

#### Table of Contents
1. [Description](#description)
1. [Requirements](#requirements)
1. [Platforms - which platforms are supported](#platforms)
    * [Which Chef version is compatible?](#chef)
    * [Prerequisites](#cookbooks)
1. [Attributes](#attributes)
1. [Usage](#usage)
1. [How to contribute](#contributing)

## Description

**ilorest** is a Chef cookbook that installs the [Python ilorest library](https://github.com/HewlettPackard/python-ilorest-library) and runs a handful of examples included in the library. Currently ilorest works with Windows Server and any 'nix distribution.

**ilorest** was written primarily as an example for server administrators to use as a template or basis for writing their own modules using the ilorest library. ilorest installs the ilorest library as part of the installation to preserve idempotency along with managing the example scripts.

### What does ilorest do?

**ilorest** starts by installing the python ilorest library through the usage of pip install. It has been set to be idempotent and supports multiple runs. Additionally, it also copies the required files into the node's cache. Subsequently, it runs a few examples with either default or set attributes. These examples are ex09, ex03, and ex14. Find MAC address, Change a bios setting, and managing a user session.

**Note:** These examples have been slightly modified from the originals. They support arguments passing the iLO credentials.

## Requirements

**ilorest** requires the node to have Python version 2.7.11+ installed for ilorest to work properly. It is suggested that `poise-python` be used for python installation and management.

It is strongly suggested by Chef and us that chef-client be run as root or administrator, to ensure that everything is working properly. If root/administrator is not used, **ilorest** may fail.

### Platforms

- Windows Server 2012, Ubuntu, Red Hat Linux

### Chef

- Chef 12.0 or later

### Cookbooks

- `poise-python` - ilorest needs python to be pre-installed.

## Attributes

### ilorest::default

These are default values that ilorest is set to.

<table>
  <tr>
    <th>Key</th>
    <th>Type</th>
    <th>Description</th>
    <th>Default</th>
  </tr>
  <tr>
    <td><tt>['ilorest']['iLO_IP']</tt></td>
    <td>String</td>
    <td>IP address of the node's iLO</td>
    <td><tt>10.0.0.100</tt></td>
  </tr>
    <tr>
    <td><tt>['ilorest']['iLO_username']</tt></td>
    <td>String</td>
    <td>username to login to the node's iLO</td>
    <td><tt>admin</tt></td>
  </tr>
    <tr>
    <td><tt>['ilorest']['iLO_password']</tt></td>
    <td>String</td>
    <td>password to login to the node's iLO</td>
    <td><tt>password</tt></td>
  </tr>
</table>

## Usage

### ilorest::default

include `ilorest` in your node's `run_list` to use the default values.

It is suggested that the attributes be edited before using since the default iLO IP address is unlikely to be the same as your node's. See the attribute example below for help in setting the attributes in JSON format.

**Attribute example**

Below is an example of what the attributes should look like when edit attributes is selected through the Chef Manage UI.

```json
{
  "ilorest": {
    "iLO_IP" : "16.1.1.10",
    "iLO_username": "admin",
    "iLO_password": "password",
  }
}
```

## Replacing examples

Examples can be easily added or replaced by following the format for the execute resource. newexample.py should be replaced with the new script you want to execute. live_stream is set to true here to show an output. The `#{platformdirectory}` variable is set depending on the platform running this module, and the `['ilorest']` attributes are set in the default.rb in the attribute's folder, or set through the use of `knife` or through the Chef Management UI.

``` ruby
execute "new example" do
  command "newexample.py #{node['ilorest']['iLO_IP']} #{node['ilorest']['iLO_username']} #{node['ilorest']['iLO_password']}"
  cwd "#{platformdirectory}"
  live_stream true
end
```

**Note:** live_stream is set to true to produce log results. 

## Contributing


1. Fork the repository on Github
2. Create a named feature branch (like `add_component_x`)
3. Write your change
4. Write tests for your change (if applicable)
5. Run the tests, ensuring they all pass
6. Submit a Pull Request using Github

## History

* 01/10/2017: Initial Commit

## License

Copyright 2017 Hewlett Packard Enterprise Development LP

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Authors

* [Jack Garcia](http://github.com/LumbaJack)
* [Matthew Kocurek](http://github.com/Yergidy)
* [Prithvi Subrahmanya](http://github.com/PrithviBS)

