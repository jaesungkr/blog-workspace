	.build_version macos, 26, 0	sdk_version 26, 5
	.section	__TEXT,__text,regular,pure_instructions
	.globl	_add                            ; -- Begin function add
	.p2align	2
_add:                                   ; @add
	.cfi_startproc
; %bb.0:
	add	w0, w1, w0
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_absolute_value                 ; -- Begin function absolute_value
	.p2align	2
_absolute_value:                        ; @absolute_value
	.cfi_startproc
; %bb.0:
	cmp	w0, #0
	cneg	w0, w0, mi
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_load_plus_one                  ; -- Begin function load_plus_one
	.p2align	2
_load_plus_one:                         ; @load_plus_one
	.cfi_startproc
; %bb.0:
	ldr	w8, [x0]
	add	w0, w8, #1
	ret
	.cfi_endproc
                                        ; -- End function
	.globl	_add_then_double                ; -- Begin function add_then_double
	.p2align	2
_add_then_double:                       ; @add_then_double
	.cfi_startproc
; %bb.0:
	stp	x29, x30, [sp, #-16]!           ; 16-byte Folded Spill
	mov	x29, sp
	.cfi_def_cfa w29, 16
	.cfi_offset w30, -8
	.cfi_offset w29, -16
	bl	_add
	lsl	w0, w0, #1
	ldp	x29, x30, [sp], #16             ; 16-byte Folded Reload
	ret
	.cfi_endproc
                                        ; -- End function
.subsections_via_symbols
