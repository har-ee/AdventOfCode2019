import System.IO
import Data.List

main = do
     g <- readFile "./input"
     let l = lines(g)
     let m = map (read::String->Int) l
     let n = map calcFuel m
     let o = sum n
     print o

calcFuel :: Int -> Int
calcFuel (i)
    |(i > 0) = (i `div` 3 - 2) + calcFuel(i `div` 3 - 2)
    |(i < 0) = -i --To balance out the negative fuel
    |otherwise = 0
