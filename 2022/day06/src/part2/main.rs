use std::{
    collections::{HashSet, VecDeque},
    env, fs, io,
};

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("you must provide input file path as parameter",);
        std::process::exit(1);
    }
    let filename = &args[1];

    let input = fs::read_to_string(filename).expect("Should have been able to read the file");
    let mut letters: VecDeque<String> = VecDeque::new();

    let mut num_letter = 0;
    for c in input.chars() {
        num_letter += 1;
        let letter = c.clone().to_string();
        letters.push_back(letter);
        if num_letter < 14 {
            continue;
        }
        if letters.len() > 14 {
            letters.remove(0);
        }

        let uniq: HashSet<String> = HashSet::from_iter(letters.iter().cloned());
        if letters.len() == uniq.len() {
            println!("marker found at pos {} ", num_letter);
            break;
        }
    }
    Ok(())
}
