#create a file name /tmp/school
file { '/tmp/school':
  ensure  => 'present',       # Ensure the file exists
  content => 'I love Puppet', # Content to be written in the file
  owner   => 'www-data',      # Set the owner to www-data
  group   => 'www-data',      # Set the group to www-data
  mode    => '0744',          # Set the file permissions to 0744
}
