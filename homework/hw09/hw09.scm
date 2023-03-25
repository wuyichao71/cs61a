(define-macro (when condition exprs)
  (list 'if condition (cons 'begin exprs) '(quote okay)))

(define-macro (switch expr cases)
  (cons 'cond
        (map (lambda (case)
                        (cons (list 'equal? expr (list 'quote (car case))) (cdr case)))
             cases)))
