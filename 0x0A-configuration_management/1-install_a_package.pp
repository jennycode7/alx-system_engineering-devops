#installs flask
exec { 'install_flask':
  command => 'pip3 install flask==2.1.0',  # Command to install Flask version 2.1.0
  path    => ['/usr/bin', '/bin'],         # Ensure correct path for pip3
  unless  => 'pip3 show flask | grep "Version: 2.1.0"',  # Prevents re-installation if version 2.1.0 is already installed
}
