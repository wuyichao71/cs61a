(define (make-or expr1 expr2)
    `(let ((v1 ,expr1))
        (if v1 v1 ,expr2))
    )

(define or-program (make-or '(print 'bork) '(/ 1 0)))
(eval or-program)
(eval (make-or '(= 1 0) '(+ 1 2)))
