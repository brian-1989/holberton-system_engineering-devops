# This script does point 2 with puppet.
exec {'exec_~/.ssh/holberton':
    command => 'echo "IdentityFile ~/.ssh/holberton" >> /etc/ssh/ssh_config',
    path    => '/bin',
}

exec { 'exec_password':
  command => "sed -i 's/#   PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/ssh_config",
  path    => '/bin',
}
