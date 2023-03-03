(define (vir-fib n)
    (if (or (= n 0) (= n 1)) n (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
)

(expect (vir-fib 10) 55)
(expect (vir-fib 1) 1)
