(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cddr s))
)

(define (swap expr)
    (let ((op (car expr))
        (first (car (cdr expr)))
        (second (caddr expr))
        (rest (cdr (cddr expr))))
      (if (> (eval second) (eval first)) (cons op (cons second (cons first rest)))
	  expr)
    )
    )

(swap '(- 1 (+ 3 5) 7 9))
(swap '(* (+ 1 1) (- 2 1)))
