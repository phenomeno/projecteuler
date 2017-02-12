answer = (1...1000).inject(0) do |sum, n|
  sum += n if n % 3 == 0 || n % 5 == 0
  sum
end

p answer
