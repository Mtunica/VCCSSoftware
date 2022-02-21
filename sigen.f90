
subroutine sigen(file_name, nx, ny,nz, charge)

	implicit none

	!Inputs: file_name
	character (len = 40) file_name;
	double precision, dimension(10000000) :: x, y, z
	double precision, dimension(8) :: xi, yi, zi
	double precision :: a, b, c, xlo, xhi, ylo,yhi,zlo,zhi,charge
	integer :: i, n, nx, ny, nz, ix, iy, iz,atom_types

	!f2py3 intent(in):: file_name, nx, ny, nz, charge
	!read(5,*) nx, ny, nz

	atom_types = 1
	charge = 0.063
	
	a = 5.5403
	b = 5.5403
	c = 5.5403

	xlo = 0.0
	xhi = nx*a+xlo
	ylo = 0.0
	yhi = ny*b+ylo
	zlo = 0.0
	zhi = nz*c+zlo

! For germanium

!   a = 5.778474 
!   b = 5.778474
!   c = 5.778474

!   a = 1.0d0 / float( nx )
!   b = 1.0d0 / float( ny )
!   c = 1.0d0 / float( nz )
	
	xi(1) = 0.0
	yi(1) = 0.0
	zi(1) = 0.0
	xi(2) = xi(1) + 0.25
	yi(2) = yi(1) + 0.25
	zi(2) = zi(1) + 0.25
	xi(3) = 0.0
	yi(3) = 0.5
	zi(3) = 0.5 
	xi(5) = 0.5
	yi(5) = 0.5
	zi(5) = 0.0
	xi(6) = xi(3) + 0.25
	yi(6) = yi(3) + 0.25
	zi(6) = zi(3) + 0.25
	xi(7) = 0.5
   	yi(7) = 0.0
   	zi(7) = 0.5
	xi(4) = xi(7) + 0.25
   	yi(4) = yi(7) + 0.25
   	zi(4) = zi(7) + 0.25
   	xi(8) = xi(5) + 0.25
   	yi(8) = yi(5) + 0.25
   	zi(8) = zi(5) + 0.25

   	n = 1

   	do iz = 0, nz - 1
   		do ix = 0, nx - 1
   			do iy = 0, ny - 1
				do i = 1, 8
					x(n) = ( ix + xi(i) ) * a
					y(n) = ( iy + yi(i) ) * b
					z(n) = ( iz + zi(i) ) * c

         			n = n + 1
       			end do
   			end do
		end do
   	end do
	!Computing number of atoms.
   	n = n - 1

	!Open file
   	open(12,file=file_name)
	
	!Writing atom_style
	write(12,'(a)') 'LAMMPS coordinates with atom_style = atomic'
	write(12,*)
	
	!Writing number of atoms
	write(12, '(I10,1x,a)') n, 'atoms'
	write(12,*)
	
	!Writing atom types
	write(12, '(I2,1x,a)') atom_types, "atom types"
	write(12,*)
	
	!Writing box dimensions
	write(12, '(2(f15.7,3x),2(a5,3x))') xlo, xhi, "xlo", "xhi"
	write(12, '(2(f15.7,3x),2(a5,3x))') ylo, yhi, "ylo", "yhi"
	write(12, '(2(f15.7,3x),2(a5,3x))') zlo, zhi, "zlo", "zhi"
	write(12,*)
	
	!Writing masses
	write(12, "(a)") "Masses"
	write(12, "(I2,1x,f11.4)") 1, 28.0855
	write(12,*)
	
	write(12,"(a)") "Atoms"
   	do i = 1, n
      	write(12,'(I10,1x,I2,1x,3(f12.5,2x),f10.3)')i,1,x(i),y(i),z(i),charge
	end do

	close(12)

end subroutine sigen
