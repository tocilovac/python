CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  phone_number TEXT,
  email TEXT UNIQUE NOT NULL,
  address TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO users (name, age, phone_number, email, address) VALUES
('Ava Nazari', 28, '050-1234567', 'ava.nazari@email.com', 'Dubai Marina, Tower 2'),
('Reza Ahmadi', 34, '055-9876543', 'reza.ahmadi@email.com', 'Jumeirah Beach Residence'),
('Sara Jafari', 25, '052-9988776', 'sara.jafari@email.com', 'Business Bay, Building 10'),
('Ali Moradi', 31, '054-1112233', 'ali.moradi@email.com', 'Downtown Dubai, Burj View'),
('Niloofar Kiani', 27, '056-4455667', 'niloofar.kiani@email.com', 'Al Barsha South'),
('Hamed Shariati', 40, '058-6677889', 'hamed.shariati@email.com', 'Palm Jumeirah, Villa 5'),
('Mina Fathi', 29, '050-3344556', 'mina.fathi@email.com', 'Dubai Silicon Oasis'),
('Kian Hosseini', 35, '055-7766554', 'kian.hosseini@email.com', 'Dubai Media City'),
('Farzaneh Ranjbar', 32, '052-4433221', 'farzaneh.ranjbar@email.com', 'Deira, Block C'),
('Mohammad Tavakoli', 45, '054-8899001', 'mohammad.tavakoli@email.com', 'Al Nahda Heights');

drop table users;