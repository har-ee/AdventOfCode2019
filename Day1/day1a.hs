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
calcFuel i = i `div` 3 - 2
