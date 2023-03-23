(define (pow-expr n p)
  (if (= p 0) 1
      `(* ,(pow-expr n (- p 1)) ,n)))
(define expr (pow-expr 5 1))
expr
(eval expr)

(define expr2 (pow-expr 5 2))
expr2
(eval expr2)

(define expr10 (pow-expr 5 10))
expr10
(eval expr10)
