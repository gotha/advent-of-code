use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("input.txt")?;
    let reader = BufReader::new(file);

    let mut curr_elf_calories: u64 = 0;
    let mut all_calories: Vec<u64> = Vec::new();

    for line in reader.lines() {
        let val: String = line?;
        if val.is_empty() {
            all_calories.push(curr_elf_calories);
            curr_elf_calories = 0;
            continue;
        }
        let calories: u64 = val.trim().parse().expect("could not parse line to integer");
        curr_elf_calories = curr_elf_calories+ calories
    }

    all_calories.sort();
    let num_elfs = all_calories.len();
    let last_three_elfs: Vec<u64> = (&all_calories[num_elfs-3 .. num_elfs]).to_vec();
    let leaders_calories: u64 = last_three_elfs.iter().sum();

    //println!("{:?}", all_calories);
    //println!("{:?}", last_three_elfs);
    println!("{:?}", leaders_calories);

    Ok(())
}
