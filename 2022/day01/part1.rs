use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut curr_calories: u64 = 0;
    let mut most_calories: u64 = 0;

    for line in reader.lines() {
        let val: String = line?;
        if val.is_empty() {
            if curr_calories > most_calories {
                most_calories = curr_calories;
            }
            curr_calories = 0;
            continue;
        }
        let calories: u64 = val.trim().parse().expect("could not parse line to integer");
        curr_calories += calories;
    }

    println!("{}", most_calories);
    Ok(())
}
