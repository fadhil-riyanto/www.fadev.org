# How Rust into() Box + Error analysis

suppose, we have function return signature like this

```rust
std::result::Result<Option<Frame>, Box<dyn std::error::Error + Send + Sync>>
```
and then, we return something like this from our function
```rust
return Err("connection reset".into())
```

how the `into()` works?

# analysis
look at [this](https://github.com/rust-lang/rust/blob/6e830462330a9e34d8176e86d4580dd0820c6fd5/library/alloc/src/boxed/convert.rs#L658) snippet
```rust
#[cfg(not(no_global_oom_handling))]
#[stable(feature = "rust1", since = "1.0.0")]
impl<'a> From<&str> for Box<dyn Error + Send + Sync + 'a> {
    /// Converts a [`str`] into a box of dyn [`Error`] + [`Send`] + [`Sync`].
    ///
    /// [`str`]: prim@str
    ///
    /// # Examples
    ///
    /// ```
    /// use std::error::Error;
    /// use std::mem;
    ///
    /// let a_str_error = "a str error";
    /// let a_boxed_error = Box::<dyn Error + Send + Sync>::from(a_str_error);
    /// assert!(
    ///     mem::size_of::<Box<dyn Error + Send + Sync>>() == mem::size_of_val(&a_boxed_error))
    /// ```
    #[inline]
    fn from(err: &str) -> Box<dyn Error + Send + Sync + 'a> {
        From::from(String::from(err))
    }
}
```

if we go deeper into `From::from`, we found [this](https://github.com/rust-lang/rust/blob/6e830462330a9e34d8176e86d4580dd0820c6fd5/library/alloc/src/boxed/convert.rs#L608)

```rust
#[inline]
    fn from(err: String) -> Box<dyn Error + Send + Sync + 'a> {
        struct StringError(String);

        impl Error for StringError {
            #[allow(deprecated)]
            fn description(&self) -> &str {
                &self.0
            }
        }

        impl fmt::Display for StringError {
            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
                fmt::Display::fmt(&self.0, f)
            }
        }

        // Purposefully skip printing "StringError(..)"
        impl fmt::Debug for StringError {
            fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
                fmt::Debug::fmt(&self.0, f)
            }
        }

        Box::new(StringError(err))
    }
```

nb: actually StringError is string aliases. then, we see in this section. we created a heap-allocated using `Box::new(StringError(err))`.
