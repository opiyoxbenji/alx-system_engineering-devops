# 
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:bin/'
} ->

# restarts nginx
exec { 'nginx-restart':
  command => 'nginz restart',
  path    => '/etc/init.d/'
}
