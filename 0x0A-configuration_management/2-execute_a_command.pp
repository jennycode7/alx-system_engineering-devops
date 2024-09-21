#kills a process
exec { 'kill_killmenow_process':
  command => 'pkill killmenow',  # Command to kill the process
  onlyif  => 'pgrep killmenow',   # Ensures the process is running before trying to kill it
  path    => ['/usr/bin', '/bin'], # Ensures Puppet knows where to find pkill and pgrep
}
