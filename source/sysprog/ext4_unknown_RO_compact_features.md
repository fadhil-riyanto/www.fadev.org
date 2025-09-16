# ext4 unknown RO compact features

this error come from linux kernel

```c
	/* Check that feature set is OK for a read-write mount */
	if (ext4_has_unknown_ext4_ro_compat_features(sb)) {
		ext4_msg(sb, KERN_ERR, "couldn't mount RDWR because of "
			 "unsupported optional features (%x)",
			 (le32_to_cpu(EXT4_SB(sb)->s_es->s_feature_ro_compat) &
				~EXT4_FEATURE_RO_COMPAT_SUPP));
		return 0;
	}
```

which EXT4_FEATURE_RO_COMPAT_SUPP

```c
#define EXT4_FEATURE_RO_COMPAT_SUPP	(EXT4_FEATURE_RO_COMPAT_SPARSE_SUPER| \
					 EXT4_FEATURE_RO_COMPAT_LARGE_FILE| \
					 EXT4_FEATURE_RO_COMPAT_GDT_CSUM| \
					 EXT4_FEATURE_RO_COMPAT_DIR_NLINK | \
					 EXT4_FEATURE_RO_COMPAT_EXTRA_ISIZE | \
					 EXT4_FEATURE_RO_COMPAT_BTREE_DIR |\
					 EXT4_FEATURE_RO_COMPAT_HUGE_FILE |\
					 EXT4_FEATURE_RO_COMPAT_BIGALLOC |\
					 EXT4_FEATURE_RO_COMPAT_METADATA_CSUM|\
					 EXT4_FEATURE_RO_COMPAT_QUOTA |\
					 EXT4_FEATURE_RO_COMPAT_PROJECT |\
					 EXT4_FEATURE_RO_COMPAT_VERITY |\
					 EXT4_FEATURE_RO_COMPAT_ORPHAN_PRESENT)
```

```c
#define EXT4_FEATURE_RO_COMPAT_GDT_CSUM		0x0010
```

[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/ext4/ext4.h#n2188](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/ext4/ext4.h#n2188)


[https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/ext4/ext4.h#n2024](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/fs/ext4/ext4.h#n2024)