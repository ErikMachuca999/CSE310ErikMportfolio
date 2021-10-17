use rand::Rng;
use std::cmp::Ordering; // allthis to use randomizing pick, ordering the numbers and user input
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101); // uses number list from 1-100 for picking number to guess

    loop {
        println!("Please input your guess.");

        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
    
        let guess: u32 = match guess.trim().parse() {
            Ok(num) => num,    // error handling
            Err(_) => continue,
        };

        println!("You guessed: {}", guess);

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => { 
                println!("You win!"); // makes the calculation of how close your number is and stops when correct
                break; // ends when input is as correct answer
            }
        }
    }
}
