; Name: Thuong Nguyen
; Course: CSC 3310
; Assignment: Scheme Game - blackjack
; Date: 11/25/2022

(newline)
(display "Welcome to our humble blackjack game")
(newline)
(display "enter (start) to begin.")
(newline)

(define (start)
    (display "Let's start with your hand: ")
    (newline)
    (game-check (take-card (+ (ran 10) 1)) (opponent-card))
)

(define (ran a)
    (random a)
)

(define (game-check a b)
    (display "They have: ")
    (display b)
    (newline)
    (if (> a 21)
        (display "They win.")
        (if (= a b)
            (display "Its a draw.")
            (if (< a b)
                (display "They win.")
                (display "You win.")
            )
        )
    )
)

(define (take-card a) 
    (let ((b (+ (ran 10) 1)))
        (display a)
        (newline)
        (display "Opponent drew their card.")
        (newline)
        (display "Would you draw more? (press 5 to draw)")
        (let ((user-input (read)))
            (if (equal? user-input 5) 
                (take-card (+ a b))
                (* 1 a)
            )
        )
    )
)

(define (opponent-card)
    (+ (ran 7) 15)
)

