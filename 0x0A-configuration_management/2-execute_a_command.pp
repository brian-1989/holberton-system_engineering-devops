# This scrip process kill.
exec {'process kill':
  command => 'pkill killmenow',
  provider => 'shell',
}
