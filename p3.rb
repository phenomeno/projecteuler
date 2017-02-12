n = 600851475143
s = Math.sqrt(n)

(1..s).reverse_each do |i|
  next unless n % i == 0

  # check if prime
  start = i / 2
  is_prime = true

  (2...start).each do |j|
    if i % j == 0
      is_prime = false
      break
    end
  end

  if is_prime
    p i
    break
  end
end
