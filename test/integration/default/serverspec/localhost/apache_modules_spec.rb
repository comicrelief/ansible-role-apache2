require 'spec_helper'

describe file("/etc/apache2/mods-enabled/remoteip.load") do
  it { should be_file }
  it { should contain("LoadModule remoteip_module /usr/lib/apache2/modules/mod_remoteip.so") }
  it { should be_linked_to '../mods-available/remoteip.load' }
end

describe file("/etc/apache2/mods-enabled/rewrite.load") do
  it { should be_file }
  it { should contain("LoadModule rewrite_module /usr/lib/apache2/modules/mod_rewrite.so") }
  it { should be_linked_to '../mods-available/rewrite.load' }
end

# Check if rewrite module is enabled
describe command("a2enmod rewrite") do
  its(:stdout) { should match("Module rewrite already enabled") }
end

# Check if remoteip module is enabled
describe command("a2enmod remoteip") do
  its(:stdout) { should match("Module remoteip already enabled") }
end

