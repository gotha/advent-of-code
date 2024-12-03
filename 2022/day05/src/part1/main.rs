#[macro_use]
extern crate lazy_static;

use regex::Regex;
use std::env;
use std::fs;
use std::io;
use std::collections::HashMap;
use std::collections::hash_map::Entry;


fn main() -> io::Result<()> {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("you must provide input file path as parameter",);
        std::process::exit(1);
    }
    let filename = &args[1];

    let contents = fs::read_to_string(filename).expect("Should have been able to read the file");
    let mut header_read = false;
    let mut header: Vec<&str> = Vec::new();
    let mut commands: Vec<&str> = Vec::new();
    for line in contents.lines() {
        if line == "" {
            header_read = true;
            continue;
        }
        match header_read {
            true => commands.push(line),
            false => header.push(line),
        };
    }

    let num_header_rows = header.len();
    let columns = &header[num_header_rows-1 .. num_header_rows][0];
    let mut num_stacks = 0;
    // importantly we support up to 9 stacks
    for i in columns.chars() {
        if i.to_string() == " " {
          continue;
        };
        num_stacks += 1;
    }
    header.pop();


    let mut data: HashMap<i32, Vec<&str>> = HashMap::new();

    for h in header.into_iter().rev() {
        let mut i: i32 = 0;
        while i < num_stacks {
            let start = (i as usize)*4+1;
            let item = &h[start .. start+1];
            if item == " " {
                i+=1;
                continue;
            }

            match data.entry(i) {
                Entry::Vacant(e) => {
                    let entry = e.insert(Vec::new());
                    entry.push(item);
                },
                Entry::Occupied(mut e) => {
                    e.get_mut().push(item);
                },
            };
            i+=1;
        }
    }

    lazy_static! {
        static ref RE: Regex = Regex::new(r"[a-z]+\s([0-9]+)\s[a-z]+\s([0-9]+)\s[a-z]+\s([0-9]+)").unwrap();
    }

    for c in commands.into_iter() {
        for cap in RE.captures_iter(&c) {
            let mut num: i32 = cap[1].parse().expect("could not parse to int");
            let from: i32 = cap[2].parse().expect("could not parse to int");
            let to: i32 = cap[3].parse().expect("could not parse to int");
            let from_stack_id: i32 = from-1;
            let to_stack_id: i32 = to-1;

            while num > 0 {
                let from_stack = data.get_mut(&from_stack_id).unwrap();
                let elem = from_stack.pop().unwrap();
                let to_stack = data.get_mut(&to_stack_id).unwrap();
                to_stack.push(elem);
                num-=1;
            }
        }
    }

    let mut i = 0;
    while i < num_stacks {
        let stack = data.get_mut(&i).unwrap();
        let last_crate = stack.pop().unwrap();
        print!("{}", last_crate);
        i+=1;
    }

    println!();
    Ok(())
}
