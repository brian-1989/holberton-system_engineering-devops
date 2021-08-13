# This scrip process kill.
exec {'process kill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
  provider => 'shell',
}
