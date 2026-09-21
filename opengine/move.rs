fn main() {
    let s = String::from("cut");
    let t = s;
    // s is moved. using s here would θ at compile.
    println!("moved {}", t);
}
