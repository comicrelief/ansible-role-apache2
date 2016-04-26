require 'spec_helper'


if os[:family] == 'ubuntu'

  describe '/etc/apache2/sites-enabled/' do
    it { should_not be_empty }
  end
  
# Tests the apache vhost
  describe file("/etc/apache2/sites-enabled/test.conf") do
    it { should contain("<VirtualHost *:80>") }

    it { should_not contain("<VirtualHost *:8080") }

    it { should_not contain("SSLEngine on") }

    it { should be_linked_to "../sites-available/test.conf" }

    it { should contain("ErrorLog /var/log/apache2/test-error.log").from(/<VirtualHost/).to(/<\/VirtualHost>/) }

    it { should contain("CustomLog /var/log/apache2/test-access.log combined-elb").from(/<VirtualHost/).to(/<\/VirtualHost>/) }
  end

end

# Check if anything is listening to port 80
describe port(80) do
  it { should be_listening }
end
