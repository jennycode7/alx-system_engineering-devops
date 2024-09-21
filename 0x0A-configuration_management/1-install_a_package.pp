#installs flask
package { 'flask':
  ensure   => '2.1.0',        # Specifies the version of Flask
  provider => 'pip3',         # Specifies that pip3 should be used
}
