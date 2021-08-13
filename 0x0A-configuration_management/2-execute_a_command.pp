# This scrip process kill.
exec {'kill':
  command => 'pkill killmenow',
  path    => '/usr/local/bin/:/bin/',
}
