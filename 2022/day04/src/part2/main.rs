#[macro_use]
extern crate lazy_static;

use regex::Regex;
use std::env;
use std::fs;
use std::io;

fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("you must provide input file path as parameter",);
        std::process::exit(1);
    }
    let filename = &args[1];

    let contents = fs::read_to_string(filename).expect("Should have been able to read the file");
    lazy_static! {
        static ref RE: Regex = Regex::new(r"([0-9]+)-([0-9]+),([0-9]+)-([0-9]+)\n").unwrap();
    }

    let mut count: u32 = 0;

    for cap in RE.captures_iter(&contents) {
        let e1s: u32 = cap[1].parse().expect("could not parse to int");
        let e1e: u32 = cap[2].parse().expect("could not parse to int");
        let e2s: u32 = cap[3].parse().expect("could not parse to int");
        let e2e: u32 = cap[4].parse().expect("could not parse to int");

        'outer: for x in e1s..e1e + 1 {
            for y in e2s..e2e + 1 {
                if x == y {
                    count += 1;
                    break 'outer;
                }
            }
        }
    }

    println!("{:?} elfs have nothing to do", count);
    Ok(())
}

