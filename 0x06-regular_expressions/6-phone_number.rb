#!/usr/bin/env ruby
# This script find the match of 10 digit phone number, without spaces
puts ARGV[0].match(/^\d{0,10}$/)
