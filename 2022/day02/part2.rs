use std::fs::File;
use std::io::{self, prelude::*, BufReader};

#[derive(Debug)]
#[derive(PartialEq)]
enum Weapon {
    Rock,
    Paper,
    Scissors,
}

fn main() -> io::Result<()>  {

    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut score: u64 = 0;
    let mut tmp_score: u64 = 0;

    for line in reader.lines() {
        let val = line?;
        let parts = val.split(" ").collect::<Vec<&str>>();
        let mine: Weapon;
        let theirs: Weapon;
        match parts[0] {
            "A" => theirs = Weapon::Rock,
            "B" => theirs = Weapon::Paper,
            "C" => theirs = Weapon::Scissors,
            _ => panic!("bahmaamu"),
        }

        match parts[1] {
            "X" => {
                match theirs {
                    Weapon::Rock => mine = Weapon::Scissors,
                    Weapon::Paper => mine = Weapon::Rock,
                    Weapon::Scissors => mine = Weapon::Paper,
                }
            },
            "Y" => {
                match theirs {
                    Weapon::Rock => mine = Weapon::Rock,
                    Weapon::Paper => mine = Weapon::Paper,
                    Weapon::Scissors => mine = Weapon::Scissors,
                }
            },
            "Z" => {
                match theirs {
                    Weapon::Rock => mine = Weapon::Paper,
                    Weapon::Paper => mine = Weapon::Scissors,
                    Weapon::Scissors => mine = Weapon::Rock,
                }
            },
            _ => panic!("bahmaamu"),
        }

        match mine {
            Weapon::Rock => tmp_score += 1,
            Weapon::Paper => tmp_score += 2,
            Weapon::Scissors => tmp_score += 3,
        }

        print!("mine: {:?}, theirs: {:?}; res: ", mine, theirs);

        let is_win = is_win(mine, theirs);
        match is_win {
            Some(res) => {
                if res == true {
                    print!("win");
                    tmp_score += 6;
                } else {
                    print!("lose");
                }
                score += tmp_score;
                tmp_score = 0
            },
            None => {
                tmp_score += 3;
                print!("draw");
            },
        }
        println!("; score: {}", score);
    }
    if tmp_score > 0 {
        score += tmp_score;
    }
    println!("final score: {}", score);

    Ok(())
}

fn is_win(mine: Weapon, theirs: Weapon) -> Option<bool> {
    if mine == theirs {
        return None
    }
    if mine == Weapon::Rock && theirs == Weapon::Scissors {
        return Some(true)
    }

    if mine == Weapon::Paper && theirs == Weapon::Rock {
        return Some(true);
    }

    if mine == Weapon::Scissors && theirs == Weapon::Paper {
        return Some(true);
    }

    return Some(false);
}
