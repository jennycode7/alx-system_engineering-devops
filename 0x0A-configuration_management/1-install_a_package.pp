#installs flask
package { 'flask':
  ensure   => '2.1.0',        # Specifies the version of Flask
  provider => 'pip3',         # Specifies that pip3 should be used
}

package { 'werkzeug':
  ensure   => '2.1.0',    # Downgrade to Werkzeug 2.1.0
  provider => 'pip3',
}
