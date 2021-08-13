# This scrip process kill.
exec {'process kill':
  command => 'pkill -f killmenow',
  path    => '/usr/local/bin/:/bin/',
}
