def palindrome?(n)
  str = n.to_s
  str == str.reverse
end

lower_limit = 700
maximum = 1

(lower_limit..1000).reverse_each do |i|
  (lower_limit..1000).reverse_each do |j|
    mul = i * j
    if palindrome?(mul)
      if mul > maximum
        maximum = mul
      end
    end
  end
end

p maximum
