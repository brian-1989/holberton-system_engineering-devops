#!/usr/bin/env ruby
# This script find a specific range (2, 5) of the 't' character,
# with the word hbttn
puts ARGV[0].scan(/hbt{2,5}n/).join
