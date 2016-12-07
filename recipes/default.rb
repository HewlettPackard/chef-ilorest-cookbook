#
# Cookbook Name:: ilorest
# Recipe:: default
#
# Copyright (c) 2016 The Authors, All Rights Reserved.

include_recipe "ilorest::install"
include_recipe "ilorest::service"
