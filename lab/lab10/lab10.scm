(define (over-or-under num1 num2) 
    (cond
        ((< num1 num2) -1)
        ((> num1 num2)  1)
        (else           0)
    )
)

(define (make-adder num)
    (begin
        (begin
            (define (helper-func inc) (+ num inc))
            helper-func
        )
        (lambda (inc) (+ num inc))
    )
)

(define (composed f g) 
    (begin
        (lambda (x) (f (g x)))
        (begin
            (define (helper x) (f (g x)))
        helper
    )
    )


)

(define lst 
    (begin
        '((1) 2 (3 4) 5)
        (list (list 1) 2 (list 3 4) 5)
        (cons 
        (cons 1 nil) 
        (cons 2 
        (cons (cons 3 (cons 4 nil)) 
        (cons 5 nil))))
    )
)

(define (duplicate lst) 
    (if (null? lst) lst
        (begin
            (cons (car lst) (cons (car lst) (duplicate (cdr lst))))
            (append (list (car lst) (car lst)) (duplicate (cdr lst)))
            (append `(,(car lst) ,(car lst)) (duplicate (cdr lst)))
        ) 
    ) 
)
