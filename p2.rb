sum = 2
left = 1
right = 2
newest = 0

(3..Float::INFINITY).lazy.each do
  newest = left + right
  break if newest > 4_000_000

  left = right
  right = newest

  sum += newest if newest % 2 == 0
end

p sum
