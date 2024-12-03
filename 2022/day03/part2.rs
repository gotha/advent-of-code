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
    let mut group = Vec::new();

    for line in reader.lines() {
        let val = line?;

        group.push(val);
        if group.len() < 3 {
            continue;
        }

        'first_loop: for a in group[0].chars() {
            let mut found: u32 = 0;
            for b in group[1].chars() {
                if a == b {
                    found+=1;
                }
                for c in group[2].chars() {
                    if found > 0 && a == c {
                        *data.entry(a).or_insert(0) += 1;

                        break 'first_loop
                    }
                }
            }
        }

        group = vec![];
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
