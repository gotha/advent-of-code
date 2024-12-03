use std::fs::File;
use std::io::{self, prelude::*, BufReader};
use std::collections::HashMap;

fn main() -> io::Result<()>  {

    let mut letters = ('a'..='z').into_iter().collect::<Vec<char>>();
    let mut uppercase = ('A'..='Z').into_iter().collect::<Vec<char>>();
    letters.append(&mut uppercase);

    let mut priority: HashMap<char, u32> = HashMap::new();
    let mut counter: u32 = 1;
    for i in letters {
        priority.insert(i, counter);
        counter += 1;
    }

    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut data: HashMap<char, u32> = HashMap::new();

    for line in reader.lines() {
        let val = line?;
        let line_length = val.chars().count();
        let left: String = val[0 .. line_length/2].to_string();
        let right: String = val[line_length/2 .. line_length].to_string();

        'outer: for i in left.chars() {
            for y in right.chars() {
                if i == y {
                    *data.entry(i).or_insert(0) += 1;
                    break 'outer;
                }
            }
        }
    }

    let mut total_score: u32 = 0;
    for (letter, occurences) in data {
        match priority.get(&letter) {
            Some(val) => {
                total_score+= val * occurences;
                println!("letter {:?}; occurences: {:?}; prority: {:?}; score: {:?}", letter, occurences, val, val*occurences);
            },
            None => panic!("bafmaamu"),
        }
    }
    println!("{:?}", total_score);

    Ok(())
}
