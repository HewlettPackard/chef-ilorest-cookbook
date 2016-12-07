
#Installs library
execute "install ilorest library" do
  command "pip install python-ilorest-library --force-reinstall"
  live_stream true
end
