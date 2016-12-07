

case node['platform']

when 'windows'
#do windows stuff
platformdirectory = "C:/chef/cache/cookbooks/ilorest/files"

when 'debian', 'ubuntu'
platformdirectory = "/var/chef/cache/cookbooks/ilorest/files"

when 'redhat', 'centos'
platformdirectory = "/var/chef/cache/cookbooks/ilorest/files"
#END CASE
end


#Files copied over automatically, only need to run them
#Will need a different path for debian/ubuntu
execute "run ex09" do
  command "python ex09_find_ilo_mac_address.py #{node['ilorest']['iLO_IP']} #{node['ilorest']['iLO_username']} #{node['ilorest']['iLO_password']}"
  cwd "#{platformdirectory}"
  live_stream true
end

execute "run ex03" do
  command "python ex03_change_bios_setting.py #{node['ilorest']['iLO_IP']} #{node['ilorest']['iLO_username']} #{node['ilorest']['iLO_password']}"
  cwd "#{platformdirectory}"
  live_stream true
end

execute "run ex14" do
  command "python ex14_sessions.py #{node['ilorest']['iLO_IP']} #{node['ilorest']['iLO_username']} #{node['ilorest']['iLO_password']}"
  cwd "#{platformdirectory}"
  live_stream true
end
