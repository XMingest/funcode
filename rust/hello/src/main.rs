use std::fs;
use std::io::prelude::*;
use std::net::TcpStream;
use std::net::TcpListener;
use std::thread;
use std::time::Duration;

fn main() {
    let listener = TcpListener::bind("127.0.0.1:46173").unwrap();

    for stream in listener.incoming() {
        let stream = stream.unwrap();

        handle_connection(stream);

        thread::sleep(Duration::from_secs(5));
    }
}

fn handle_connection(mut stream: TcpStream) {
    let mut buffer = [0; 1024];

    stream.read(&mut buffer).unwrap();

    println!("::REQ::\n{}", String::from_utf8_lossy(&buffer[..]));

    let contents = fs::read_to_string("index.htm").unwrap();

    let response = format!(
        "HTTP/1.1 200 OK\r\nContent-Length: {}\r\n\r\n{}",
        contents.len(),
        contents
    );

    println!("::RESP::\n{}", response);
    stream.write(response.as_bytes()).unwrap();
    stream.flush().unwrap();
}
