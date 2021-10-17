// Rust uses comment syntax the exact same as C++

// These lines define a function in Rust. 
// The first line declares a function named main
// and has no parameters in the parentheses
fn main() {                        // the function body is wrapped in curly brackets, {}. 
    println!("Hello, world!");     // Rust requires these around all function bodies.
}
// within a function, the indention in Rust style is IN FOUR SPACES, NOT a tab.

// println! calls a Rust macro. If it called a function  
// instead, it would be entered as println (without the !)
// using a ! means that you’re calling a macro instead of 
// a normal function.

// the "Hello, world!" string is passed in the function; this string as an 
// argument to println!, and the string is printed to the screen.
// then ends the line with a semicolon (;), 
// and close the function with the closing curly braces

// Before running a Rust program, you must compile it using the Rust compiler
// by entering the rustc command and passing it the name of your source file. 
// example: rustc (name_of_file.rs) but dont include parentheses
// then typing .\(name_of_file).exe) crucial, the .exe